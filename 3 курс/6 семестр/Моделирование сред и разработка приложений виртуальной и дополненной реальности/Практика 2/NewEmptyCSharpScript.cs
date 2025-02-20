using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomMove : MonoBehaviour
{
    public Vector3[] points;
    private int currentPointIndex = 0;

    void Start()
    {
        points = new Vector3[]
        {
            new Vector3(0, 0, 0),
            new Vector3(5, 0, 0),
            new Vector3(0, 5, 0),
            new Vector3(5, 5, 0)
        };
    }

    void Update()
    {
        int randomNumber = Random.Range(1, 6);

        if (randomNumber == 5)
        {
            MoveToNextPoint();
        }
    }

    void MoveToNextPoint()
    {
        if (points.Length == 0)
        {
            Debug.LogWarning("No points assigned.");
            return;
        }

        transform.position = points[currentPointIndex];

        currentPointIndex = (currentPointIndex + 1) % points.Length;
    }
}