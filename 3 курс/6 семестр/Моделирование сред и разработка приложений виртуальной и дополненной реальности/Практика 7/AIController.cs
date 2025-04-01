using UnityEngine.AI;
using UnityEngine;

public class AIController : MonoBehaviour
{
    public Transform playerTarget;
    private NavMeshAgent agent;
    public float chaseDistance = 10f;
    public float stoppingDistance = 2f;

    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        if (playerTarget == null)
            playerTarget = GameObject.FindGameObjectWithTag("Player").transform;
    }

    void Update()
    {
        if (playerTarget == null) return;

        float distance = Vector3.Distance(transform.position, playerTarget.position);

        if (distance <= chaseDistance)
        {
            agent.SetDestination(playerTarget.position);
        }
    }
}