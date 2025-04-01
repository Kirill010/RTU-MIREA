using UnityEngine;

[RequireComponent(typeof(Animator), typeof(CharacterController))]
public class PlayerAnimation : MonoBehaviour
{
    [Header("Required References")]
    [SerializeField] private Animator animator;
    [SerializeField] private CharacterController controller;
    [SerializeField] private PlayerController2 playerController;

    [Header("Animation Thresholds")]
    [Tooltip("Minimum speed to transition from idle to walk")]
    public float walkSpeedThreshold = 0.5f;
    [Tooltip("Minimum speed to consider character running")]
    public float runSpeedThreshold = 5f;
    [Tooltip("Time buffer after leaving ground")]
    public float groundCheckBuffer = 0.15f;

    [Header("Debug")]
    public bool showDebugInfo = true;

    private float lastGroundedTime;
    private float currentSpeed;
    private bool isRunning;
    private bool isGrounded;

    void Awake()
    {
        InitializeComponents();
        ValidateAnimatorSetup();
    }

    void Update()
    {
        if (!animator.enabled || !animator.runtimeAnimatorController) return;

        CalculateMovementParameters();
        UpdateAnimatorParameters();
        HandleJumpInput();
    }

    private void InitializeComponents()
    {
        if (animator == null) animator = GetComponent<Animator>();
        if (controller == null) controller = GetComponent<CharacterController>();
        if (playerController == null) playerController = GetComponent<PlayerController2>();
    }

    private void ValidateAnimatorSetup()
    {
        if (animator.runtimeAnimatorController == null)
        {
            Debug.LogError("Animator Controller is missing!", this);
            enabled = false;
            return;
        }

        if (!animator.enabled)
        {
            Debug.LogWarning("Animator component is disabled!", this);
        }
    }

    private void CalculateMovementParameters()
    {
        // Calculate horizontal speed (ignore vertical movement)
        Vector3 horizontalVelocity = new Vector3(
            controller.velocity.x,
            0f,
            controller.velocity.z
        );
        currentSpeed = horizontalVelocity.magnitude;

        // Determine if character is running
        isRunning = playerController.IsRunning() && currentSpeed > walkSpeedThreshold;

        // Update grounded status with buffer
        bool groundedNow = controller.isGrounded;
        if (groundedNow) lastGroundedTime = Time.time;
        isGrounded = (Time.time - lastGroundedTime) < groundCheckBuffer;
    }

    private void UpdateAnimatorParameters()
    {
        animator.SetFloat("Speed", currentSpeed);
        animator.SetBool("IsRunning", isRunning);
        animator.SetBool("IsGrounded", isGrounded);

        if (showDebugInfo)
        {
            Debug.Log($"Speed: {currentSpeed:F2}, Running: {isRunning}, Grounded: {isGrounded}");
        }
    }

    private void HandleJumpInput()
    {
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            animator.SetTrigger("Jump");
            if (showDebugInfo) Debug.Log("Jump triggered");
        }
    }

    // Called via Animation Event at the end of jump animation
    public void OnJumpAnimationEnd()
    {
        animator.ResetTrigger("Jump");
        if (showDebugInfo) Debug.Log("Jump animation ended");
    }

    // Called via Animation Event when jump reaches peak height
    public void OnJumpPeakReached()
    {
        // Can add additional logic here if needed
    }
}