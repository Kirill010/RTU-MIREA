using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

[RequireComponent(typeof(CharacterController), typeof(Animator))]
public class PlayerController3 : MonoBehaviour
{
    [Header("Movement Settings")]
    public float walkSpeed = 5f;
    public float runSpeed = 8f;
    public float crouchSpeed = 2.5f;
    public float gravity = 20f;
    public float jumpForce = 8f;
    public float rotationSpeed = 10f;
    public float groundCheckDistance = 0.2f;

    [Header("Camera Settings")]
    public Vector3 thirdPersonOffset = new Vector3(-20, 10, 0);
    public Vector3 firstPersonOffset = new Vector3(0, 1.15f, 0);
    public float mouseSensitivity = 2f;
    public float cameraPitchLimit = 30f;
    public Transform cameraTransform;
    public KeyCode viewSwitchKey = KeyCode.V;

    [Header("Health Settings")]
    public int maxHealth = 10;
    public int jumpDamage = 1;
    public Slider healthBar;
    public float damageCooldown = 0.5f;

    [Header("Animation Settings")]
    public float animationSmoothTime = 0.1f;

    private CharacterController controller;
    private Animator animator;
    private float verticalVelocity;
    private int currentHealth;
    private float cameraPitch;
    private float lastDamageTime;
    private float originalHeight;
    private Vector3 originalCenter;
    private bool isCrouching;
    private Vector3 moveDirection = Vector3.zero;
    private float animationBlend;
    private float targetAnimationBlend;
    private float animationBlendVelocity;
    private bool isFirstPersonView = false;

    void Start()
    {
        controller = GetComponent<CharacterController>();
        animator = GetComponent<Animator>();
        originalHeight = controller.height;
        originalCenter = controller.center;

        currentHealth = maxHealth;
        InitializeHealthBar();

        if (cameraTransform == null)
            cameraTransform = Camera.main.transform;

        Cursor.lockState = CursorLockMode.Locked;
        UpdateCameraPosition();
    }

    void Update()
    {
        if (animator == null || !animator.enabled) return;
        bool isGrounded = CheckGrounded();
        animator.SetBool("IsGrounded", isGrounded);

        HandleViewSwitch();
        HandleMouseLook();
        HandleMovement();
        HandleJump();
        HandleCrouch();
        HandleFallRespawn();
        UpdateAnimations();
    }

    void HandleViewSwitch()
    {
        if (Input.GetKeyDown(viewSwitchKey))
        {
            isFirstPersonView = !isFirstPersonView;
            UpdateCameraPosition();
        }
    }

    void UpdateCameraPosition()
    {
        cameraTransform.localPosition = isFirstPersonView ? firstPersonOffset : thirdPersonOffset;
        cameraTransform.localEulerAngles = Vector3.right * cameraPitch;
        cameraTransform.LookAt(transform);
    }

    bool CheckGrounded()
    {
        return Physics.Raycast(transform.position, Vector3.down, groundCheckDistance);
    }

    void InitializeHealthBar()
    {
        if (healthBar != null)
        {
            healthBar.maxValue = maxHealth;
            healthBar.value = currentHealth;
        }
    }

    void HandleMouseLook()
    {
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        transform.Rotate(Vector3.up, mouseX * rotationSpeed * Time.deltaTime);

        cameraPitch -= mouseY;
        cameraPitch = Mathf.Clamp(cameraPitch, -cameraPitchLimit, cameraPitchLimit);

        UpdateCameraPosition();
    }

    void HandleMovement()
    {
        float moveZ = Input.GetAxis("Vertical");
        float moveX = Input.GetAxis("Horizontal");

        Vector3 move = transform.forward * moveZ + transform.right * moveX;
        float currentSpeed = GetCurrentSpeed();

        if (controller.isGrounded)
        {
            moveDirection = move * currentSpeed;
        }

        moveDirection.y = verticalVelocity;
        controller.Move(moveDirection * Time.deltaTime);

        if (move.magnitude > 0)
        {
            targetAnimationBlend = Input.GetKey(KeyCode.LeftShift) ? 1f : 0.5f;
        }
        else
        {
            targetAnimationBlend = 0f;
        }
    }

    void UpdateAnimations()
    {
        animationBlend = Mathf.SmoothDamp(
            animationBlend,
            targetAnimationBlend,
            ref animationBlendVelocity,
            animationSmoothTime
        );

        // ќтключаем анимации в режиме от первого лица
        if (!isFirstPersonView)
        {
            animator.SetFloat("Speed", animationBlend);
        }
        else
        {
            animator.SetFloat("Speed", 0);
        }
    }

    float GetCurrentSpeed()
    {
        if (isCrouching) return crouchSpeed;
        if (Input.GetKey(KeyCode.LeftShift)) return runSpeed;
        return walkSpeed;
    }

    public bool IsGrounded()
    {
        return controller.isGrounded;
    }

    public bool IsRunning()
    {
        return Input.GetKey(KeyCode.LeftShift) && !isCrouching;
    }

    void HandleJump()
    {
        if (controller.isGrounded)
        {
            verticalVelocity = -0.5f;

            if (Input.GetKeyDown(KeyCode.Space) && IsGrounded())
            {
                verticalVelocity = jumpForce;
                animator.SetTrigger("JumpTrigger");
                TakeDamage(jumpDamage);
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
                Crouch();
            else
                StandUp();
        }
    }

    void Crouch()
    {
        controller.height = originalHeight / 2;
        controller.center = originalCenter / 2;
        isCrouching = true;

        // ќбновл€ем смещение камеры дл€ первого лица при приседании
        if (isFirstPersonView)
        {
            firstPersonOffset.y = 0.85f; // ѕоловина от обычной высоты
        }
        UpdateCameraPosition();
    }

    void StandUp()
    {
        if (!CheckCeiling())
        {
            controller.height = originalHeight;
            controller.center = originalCenter;
            isCrouching = false;

            // ¬осстанавливаем стандартное смещение камеры
            if (isFirstPersonView)
            {
                firstPersonOffset.y = 1.7f;
            }
            UpdateCameraPosition();
        }
    }

    bool CheckCeiling()
    {
        return Physics.Raycast(transform.position, Vector3.up, originalHeight / 2 + 0.2f);
    }

    void HandleFallRespawn()
    {
        if (transform.position.y < -10f)
            Respawn();
    }

    public void TakeDamage(int damage)
    {
        if (Time.time > lastDamageTime + damageCooldown)
        {
            currentHealth -= damage;
            lastDamageTime = Time.time;
            UpdateHealthUI();

            if (currentHealth <= 0)
                Die();
        }
    }

    void UpdateHealthUI()
    {
        if (healthBar != null)
            healthBar.value = currentHealth;
    }

    void Die()
    {
        Debug.Log("Player died!");
        Respawn();
    }

    void Respawn()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

    public void Heal(int amount)
    {
        currentHealth = Mathf.Min(currentHealth + amount, maxHealth);
        UpdateHealthUI();
    }
}