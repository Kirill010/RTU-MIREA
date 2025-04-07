using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerController2 : MonoBehaviour
{
    public float walkSpeed = 5f;
    public float runSpeed = 8f;
    public float crouchSpeed = 2.5f;

    public bool isFirstPerson = true;
    public Vector3 thirdPersonOffset = new Vector3(0, 2, -5);

    public float mouseSensitivity = 2f;
    public Transform cameraTransform;
    private float cameraPitch = 0f;

    public float speed = 5f;
    public float gravity = 9.81f;
    public float jumpForce = 5f;
    public int health = 10;
    public int attackPower = 10;

    private CharacterController controller;
    private Vector3 moveDirection = Vector3.zero;
    private float verticalVelocity = 0f;
    private bool isGrounded;

    private bool isCrouching = false;
    private float originalHeight;
    private Vector3 originalCenter;

    void Start()
    {
        controller = GetComponent<CharacterController>();
        originalHeight = controller.height;
        originalCenter = controller.center;

        if (cameraTransform == null)
        {
            cameraTransform = Camera.main.transform;
        }

        UpdateCameraPosition();

        SetupLayersAndCollisions();
    }

    void Update()
    {
        isGrounded = controller.isGrounded;

        HandleMouseLook();

        HandleMovement();

        HandleJump();

        HandleCrouch();

        if (transform.position.y < -10f)
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
        }

        if (Input.GetKeyDown(KeyCode.E))
        {
            Interact();
        }

        if (Input.GetKeyDown(KeyCode.V))
        {
            ToggleCameraMode();
        }
    }

    void HandleMouseLook()
    {
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        transform.Rotate(0, mouseX, 0);

        cameraPitch -= mouseY;
        cameraPitch = Mathf.Clamp(cameraPitch, -90f, 90f);

        if (isFirstPerson)
        {
            cameraTransform.localEulerAngles = new Vector3(cameraPitch, 0, 0);
        }
        else
        {
            cameraTransform.localPosition = thirdPersonOffset;
            cameraTransform.LookAt(transform);
        }
    }

    void HandleMovement()
    {
        float moveZ = Input.GetAxis("Vertical");
        float moveX = Input.GetAxis("Horizontal");
        Vector3 move = transform.forward * moveZ + transform.right * moveX;

        float currentSpeed = walkSpeed;
        bool isRunning = false;
        if (Input.GetKey(KeyCode.LeftShift))
        {
            currentSpeed = runSpeed;
            isRunning = true;
        }
        else if (Input.GetKey(KeyCode.C))
        {
            currentSpeed = crouchSpeed;
            isRunning = false;
        }

        // Передаем состояние бега в SFX_Manager
        if (SFX_Manager.Instance != null)
        {
            SFX_Manager.Instance.SetRunningState(isRunning);
        }

        moveDirection = move * currentSpeed;
        moveDirection.y = verticalVelocity;

        controller.Move(moveDirection * Time.deltaTime);
    }

    void HandleJump()
    {
        if (controller.isGrounded)
        {
            verticalVelocity = -0.5f;

            if (Input.GetKeyDown(KeyCode.Space))
            {
                verticalVelocity = jumpForce;
                LoseHealthOnJump();

                // Добавленная проверка
                if (SFX_Manager.Instance != null)
                {
                    SFX_Manager.Instance.PlayJumpSound();
                }
                else
                {
                    Debug.LogWarning("SFX_Manager instance missing!");
                }
            }
        }
        else
        {
            verticalVelocity -= gravity * Time.deltaTime;
        }
    }

    void HandleCrouch()
    {
        if (Input.GetKeyDown(KeyCode.C))
        {
            if (!isCrouching)
            {
                Crouch();
            }
            else
            {
                StandUp();
            }
        }
    }

    void Crouch()
    {
        controller.height = originalHeight / 2;
        controller.center = originalCenter / 2;
        isCrouching = true;
    }

    void StandUp()
    {
        controller.height = originalHeight;
        controller.center = originalCenter;
        isCrouching = false;
    }

    void Interact()
    {
        RaycastHit hit;
        if (Physics.Raycast(cameraTransform.position, cameraTransform.forward, out hit, 3f))
        {
            ButtonInteract button = hit.collider.GetComponent<ButtonInteract>();
            if (button != null)
            {
                button.ActivateTrap();
                SFX_Manager.Instance.PlayButtonClick();
            }
        }
    }

    void LoseHealthOnJump()
    {
        health -= 1;
        Debug.Log("Health after jump: " + health);

        if (health <= 0)
        {
            Debug.Log("Died!");
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
        }
    }

    void ToggleCameraMode()
    {
        isFirstPerson = !isFirstPerson;
        UpdateCameraPosition();
    }

    void UpdateCameraPosition()
    {
        if (isFirstPerson)
        {
            cameraTransform.localPosition = Vector3.zero;
            cameraTransform.localEulerAngles = Vector3.zero;
        }
        else
        {
            cameraTransform.localPosition = thirdPersonOffset;
            cameraTransform.LookAt(transform);
        }
    }

    void SetupLayersAndCollisions()
    {
        int playerLayer = LayerMask.NameToLayer("Player");
        int obstaclesLayer = LayerMask.NameToLayer("Obstacles");
        int backgroundLayer = LayerMask.NameToLayer("Background");

        Physics.IgnoreLayerCollision(playerLayer, backgroundLayer, true);

        Camera.main.cullingMask = ~(1 << backgroundLayer);
    }
}