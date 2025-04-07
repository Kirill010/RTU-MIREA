using UnityEngine;

public class FirstPersonCamera : MonoBehaviour
{
    public Transform player; // ������ �� ���������
    public float mouseSensitivity = 2f; // ���������������� ����
    private float cameraPitch = 0f;

    void Start()
    {
        // �������� � ��������� ������ � ������ ������
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    void Update()
    {
        // �������� ���� ����
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        // ������� ��������� �� �����������
        player.Rotate(0, mouseX, 0);

        // ������� ������ �� ���������
        cameraPitch -= mouseY;
        cameraPitch = Mathf.Clamp(cameraPitch, -90f, 90f); // ������������ ���� �������� ������
        transform.localEulerAngles = new Vector3(cameraPitch, 0, 0);
    }
}