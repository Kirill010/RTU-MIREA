using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerController : MonoBehaviour
{
    // Скорости для ходьбы, бега и приседания
    public float walkSpeed = 5f;
    public float runSpeed = 8f;
    public float crouchSpeed = 2.5f;

    // Параметры прыжка и гравитации
    public float jumpForce = 5f;
    public float gravity = 9.81f;

    // Параметры для обзора с помощью мыши
    public float mouseSensitivity = 2f;
    public Transform cameraTransform; // Ссылка на камеру
    private float cameraPitch = 0f;

    // Параметры для камеры от третьего лица
    public bool isFirstPerson = true; // Режим камеры (от первого лица или от третьего)
    public Vector3 thirdPersonOffset = new Vector3(0, 2, -5); // Смещение камеры в режиме от третьего лица

    private CharacterController controller;
    private Vector3 moveDirection = Vector3.zero;
    private float verticalVelocity = 0f;

    // Параметры для приседания
    private bool isCrouching = false;
    private float originalHeight;
    private Vector3 originalCenter;

    void Start()
    {
        controller = GetComponent<CharacterController>();
        originalHeight = controller.height;
        originalCenter = controller.center;

        // Если камера не назначена в Inspector, попытаемся найти Main Camera
        if (cameraTransform == null)
        {
            cameraTransform = Camera.main.transform;
        }

        // Настройка камеры в зависимости от режима
        if (!isFirstPerson)
        {
            cameraTransform.localPosition = thirdPersonOffset;
            cameraTransform.LookAt(transform);
        }

        // Скрываем и фиксируем курсор в центре экрана
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    void Update()
    {
        // Обработка обзора с помощью мыши
        HandleMouseLook();

        // Получение ввода для движения
        HandleMovement();

        // Обработка прыжка
        HandleJump();

        // Обработка приседания
        HandleCrouch();

        // Перезапуск уровня, если персонаж падает ниже определённой точки (например, -10 по Y)
        if (transform.position.y < -10f)
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
        }

        // Обработка взаимодействия (нажатие клавиши F)
        if (Input.GetKeyDown(KeyCode.F))
        {
            Interact();
        }
    }

    void HandleMouseLook()
    {
        // Получаем ввод мыши
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        // Поворот персонажа по горизонтали
        transform.Rotate(0, mouseX, 0);

        // Поворот камеры по вертикали
        cameraPitch -= mouseY;
        cameraPitch = Mathf.Clamp(cameraPitch, -90f, 90f); // Ограничиваем угол поворота камеры

        // Применяем поворот камеры
        if (isFirstPerson)
        {
            cameraTransform.localEulerAngles = new Vector3(cameraPitch, 0, 0);
        }
        else
        {
            // В режиме от третьего лица камера следует за персонажем
            cameraTransform.localPosition = thirdPersonOffset;
            cameraTransform.LookAt(transform);
        }
    }

    void HandleMovement()
    {
        float moveZ = Input.GetAxis("Vertical");
        float moveX = Input.GetAxis("Horizontal");
        Vector3 move = transform.forward * moveZ + transform.right * moveX;

        // Выбор текущей скорости (бег, приседание или ходьба)
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

        // Движение через CharacterController
        controller.Move(moveDirection * Time.deltaTime);
    }

    void HandleJump()
    {
        // Если персонаж стоит на земле
        if (controller.isGrounded)
        {
            verticalVelocity = -0.5f; // Небольшое отрицательное значение, чтобы персонаж прилипал к земле

            // Прыжок по нажатию пробела
            if (Input.GetKeyDown(KeyCode.Space))
            {
                verticalVelocity = jumpForce;
            }
        }
        else
        {
            // Применение гравитации
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

    // Метод для приседания
    void Crouch()
    {
        controller.height = originalHeight / 2;
        controller.center = originalCenter / 2;
        isCrouching = true;
    }

    // Метод для вставания
    void StandUp()
    {
        controller.height = originalHeight;
        controller.center = originalCenter;
        isCrouching = false;
    }

    // Пример метода взаимодействия
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