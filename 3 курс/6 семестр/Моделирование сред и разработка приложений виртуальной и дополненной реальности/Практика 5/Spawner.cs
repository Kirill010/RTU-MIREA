using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject cubePrefab;
    public int numberOfCubes = 5;
    public float spawnRadius = 3f; // ������ ������
    public float objectLifetime = 5f; // ����� ����� �������
    public float minSpawnDelay = 1.5f; // ����������� �������� ����� �������
    public float maxSpawnDelay = 5f; // ������������ �������� ����� �������

    private float nextSpawnTime;
    private int cubesSpawned;

    void Start()
    {
        ScheduleNextSpawn();
    }

    void Update()
    {
        if (Time.time >= nextSpawnTime && cubesSpawned < numberOfCubes)
        {
            SpawnCube();
            ScheduleNextSpawn();
        }
    }

    private void SpawnCube()
    {
        Vector3 spawnPosition = Random.insideUnitSphere * spawnRadius;
        spawnPosition.y = 0; // ������������� Y �� 0, ���� ����������

        GameObject newCube = Instantiate(cubePrefab, spawnPosition, Quaternion.identity);
        Destroy(newCube, objectLifetime);
        cubesSpawned++;
    }

    private void ScheduleNextSpawn()
    {
        float spawnDelay = Random.Range(minSpawnDelay, maxSpawnDelay);
        nextSpawnTime = Time.time + spawnDelay;
    }
}
