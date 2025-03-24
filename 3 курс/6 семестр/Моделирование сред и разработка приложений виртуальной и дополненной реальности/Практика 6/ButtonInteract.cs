using UnityEngine;

public class ButtonInteract : MonoBehaviour
{
    public GameObject trapPrefab; // Префаб ловушки
    public Transform spawnPoint; // Точка спавна ловушки

    private bool activated = false;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    // Метод, вызываемый при нажатии кнопки
    public void ActivateTrap()
    {
        if (!activated)
        {
            activated = true;
            Instantiate(trapPrefab, spawnPoint.position, spawnPoint.rotation);
            Debug.Log("Ловушка активирована!");
        }
        // Здесь можно добавить логику активации ловушки или другого взаимодействия
    }
}
