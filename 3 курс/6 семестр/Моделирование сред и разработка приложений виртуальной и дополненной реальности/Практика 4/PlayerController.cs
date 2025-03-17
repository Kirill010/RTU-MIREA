using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerController : MonoBehaviour
{
    // �������� ��� ������, ���� � ����������
    public float walkSpeed = 5f;
    public float runSpeed = 8f;
    public float crouchSpeed = 2.5f;

    // ��������� ������ � ����������
    public float jumpForce = 5f;
    public float gravity = 9.81f;

    // ��������� ��� ������ � ������� ����
    public float mouseSensitivity = 2f;
    public Transform cameraTransform; // ������ �� ������
    private float cameraPitch = 0f;

    // ��������� ��� ������ �� �������� ����
    public bool isFirstPerson = true; // ����� ������ (�� ������� ���� ��� �� ��������)
    public Vector3 thirdPersonOffset = new Vector3(0, 2, -5); // �������� ������ � ������ �� �������� ����

    private CharacterController controller;
    private Vector3 moveDirection = Vector3.zero;
    private float verticalVelocity = 0f;

    // ��������� ��� ����������
    private bool isCrouching = false;
    private float originalHeight;
    private Vector3 originalCenter;

    void Start()
    {
        controller = GetComponent<CharacterController>();
        originalHeight = controller.height;
        originalCenter = controller.center;

        // ���� ������ �� ��������� � Inspector, ���������� ����� Main Camera
        if (cameraTransform == null)
        {
            cameraTransform = Camera.main.transform;
        }

        // ��������� ������ � ����������� �� ������
        if (!isFirstPerson)
        {
            cameraTransform.localPosition = thirdPersonOffset;
            cameraTransform.LookAt(transform);
        }

        // �������� � ��������� ������ � ������ ������
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    void Update()
    {
        // ��������� ������ � ������� ����
        HandleMouseLook();

        // ��������� ����� ��� ��������
        HandleMovement();

        // ��������� ������
        HandleJump();

        // ��������� ����������
        HandleCrouch();

        // ���������� ������, ���� �������� ������ ���� ����������� ����� (��������, -10 �� Y)
        if (transform.position.y < -10f)
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
        }

        // ��������� �������������� (������� ������� F)
        if (Input.GetKeyDown(KeyCode.F))
        {
            Interact();
        }
    }

    void HandleMouseLook()
    {
        // �������� ���� ����
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        // ������� ��������� �� �����������
        transform.Rotate(0, mouseX, 0);

        // ������� ������ �� ���������
        cameraPitch -= mouseY;
        cameraPitch = Mathf.Clamp(cameraPitch, -90f, 90f); // ������������ ���� �������� ������

        // ��������� ������� ������
        if (isFirstPerson)
        {
            cameraTransform.localEulerAngles = new Vector3(cameraPitch, 0, 0);
        }
        else
        {
            // � ������ �� �������� ���� ������ ������� �� ����������
            cameraTransform.localPosition = thirdPersonOffset;
            cameraTransform.LookAt(transform);
        }
    }

    void HandleMovement()
    {
        float moveZ = Input.GetAxis("Vertical");
        float moveX = Input.GetAxis("Horizontal");
        Vector3 move = transform.forward * moveZ + transform.right * moveX;

        // ����� ������� �������� (���, ���������� ��� ������)
        float currentSpeed = walkSpeed;
        if (Input.GetKey(KeyCode.LeftShift))
        {
            currentSpeed = runSpeed;
        }
        else if (Input.GetKey(KeyCode.C))
        {
            currentSpeed = crouchSpeed;
        }

        moveDirection = move * currentSpeed;
        moveDirection.y = verticalVelocity;

        // �������� ����� CharacterController
        controller.Move(moveDirection * Time.deltaTime);
    }

    void HandleJump()
    {
        // ���� �������� ����� �� �����
        if (controller.isGrounded)
        {
            verticalVelocity = -0.5f; // ��������� ������������� ��������, ����� �������� �������� � �����

            // ������ �� ������� �������
            if (Input.GetKeyDown(KeyCode.Space))
            {
                verticalVelocity = jumpForce;
            }
        }
        else
        {
            // ���������� ����������
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

    // ����� ��� ����������
    void Crouch()
    {
        controller.height = originalHeight / 2;
        controller.center = originalCenter / 2;
        isCrouching = true;
    }

    // ����� ��� ���������
    void StandUp()
    {
        controller.height = originalHeight;
        controller.center = originalCenter;
        isCrouching = false;
    }

    // ������ ������ ��������������
    void Interact()
    {
        RaycastHit hit;
        if (Physics.Raycast(transform.position, transform.forward, out hit, 3f))
        {
            if (hit.collider.CompareTag("Button"))
            {
                ButtonInteract button = hit.collider.GetComponent<ButtonInteract>();
                if (button != null)
                {
                    button.ActivateTrap();
                }
            }
        }
    }
}