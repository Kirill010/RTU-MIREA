using UnityEngine;

public class UpDown : MonoBehaviour
{
    public float moveSpeed = 5f; // Скорость движения
    public float rotationSpeed = 100f; // Скорость вращения
    void Start()
    {
        
    }

    void Update()
    {
        // Движение вперед и назад
        float moveInput = Input.GetAxis("Vertical"); // W/S
        transform.Translate(Vector3.forward * moveInput * moveSpeed * Time.deltaTime);

        // Вращение влево и вправо
        float rotationInput = Input.GetAxis("Horizontal"); // A/D
        transform.Rotate(Vector3.up * rotationInput * rotationSpeed * Time.deltaTime);
    }
}
