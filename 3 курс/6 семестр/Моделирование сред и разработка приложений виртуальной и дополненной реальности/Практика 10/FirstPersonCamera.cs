using UnityEngine;

public class FirstPersonCamera : MonoBehaviour
{
    public Transform player; // Ссылка на персонажа
    public float mouseSensitivity = 2f; // Чувствительность мыши
    private float cameraPitch = 0f;

    void Start()
    {
        // Скрываем и фиксируем курсор в центре экрана
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    void Update()
    {
        // Получаем ввод мыши
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        // Поворот персонажа по горизонтали
        player.Rotate(0, mouseX, 0);

        // Поворот камеры по вертикали
        cameraPitch -= mouseY;
        cameraPitch = Mathf.Clamp(cameraPitch, -90f, 90f); // Ограничиваем угол поворота камеры
        transform.localEulerAngles = new Vector3(cameraPitch, 0, 0);
    }
}