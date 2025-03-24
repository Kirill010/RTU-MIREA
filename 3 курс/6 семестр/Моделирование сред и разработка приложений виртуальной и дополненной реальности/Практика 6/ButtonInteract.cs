using UnityEngine;

public class ButtonInteract : MonoBehaviour
{
    public GameObject trapPrefab; // ������ �������
    public Transform spawnPoint; // ����� ������ �������

    private bool activated = false;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    // �����, ���������� ��� ������� ������
    public void ActivateTrap()
    {
        if (!activated)
        {
            activated = true;
            Instantiate(trapPrefab, spawnPoint.position, spawnPoint.rotation);
            Debug.Log("������� ������������!");
        }
        // ����� ����� �������� ������ ��������� ������� ��� ������� ��������������
    }
}
