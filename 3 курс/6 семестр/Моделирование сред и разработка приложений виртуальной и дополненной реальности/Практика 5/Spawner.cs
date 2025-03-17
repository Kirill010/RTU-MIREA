using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject cubePrefab;
    public int numberOfCubes = 5;
    public float spawnRadius = 3f; // Радиус спавна
    public float objectLifetime = 5f; // Время жизни объекта
    public float minSpawnDelay = 1.5f; // Минимальная задержка между спавном
    public float maxSpawnDelay = 5f; // Максимальная задержка между спавном

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
        spawnPosition.y = 0; // Устанавливаем Y на 0, если необходимо

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
