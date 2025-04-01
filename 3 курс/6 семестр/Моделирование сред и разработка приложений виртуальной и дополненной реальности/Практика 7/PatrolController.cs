using UnityEngine;
using UnityEngine.AI;

public class PatrolController : MonoBehaviour
{
    public Transform[] waypoints;
    private NavMeshAgent _agent;
    private int _currentWaypoint;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        _agent = GetComponent<NavMeshAgent>();
        _currentWaypoint = 0;
        SetNextWaypoint();
    }

    // Update is called once per frame
    void Update()
    {
        if (_agent.remainingDistance < 0.5f)
            SetNextWaypoint();
    }

    void SetNextWaypoint()
    {
        _agent.SetDestination(waypoints[_currentWaypoint].position);
        _currentWaypoint = (_currentWaypoint + 1) % waypoints.Length;
    }
}
