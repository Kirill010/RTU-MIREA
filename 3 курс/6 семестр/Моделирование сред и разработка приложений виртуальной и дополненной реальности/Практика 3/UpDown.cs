using UnityEngine;

public class UpDown : MonoBehaviour
{
    public float moveSpeed = 5f; // �������� ��������
    public float rotationSpeed = 100f; // �������� ��������
    void Start()
    {
        
    }

    void Update()
    {
        // �������� ������ � �����
        float moveInput = Input.GetAxis("Vertical"); // W/S
        transform.Translate(Vector3.forward * moveInput * moveSpeed * Time.deltaTime);

        // �������� ����� � ������
        float rotationInput = Input.GetAxis("Horizontal"); // A/D
        transform.Rotate(Vector3.up * rotationInput * rotationSpeed * Time.deltaTime);
    }
}
