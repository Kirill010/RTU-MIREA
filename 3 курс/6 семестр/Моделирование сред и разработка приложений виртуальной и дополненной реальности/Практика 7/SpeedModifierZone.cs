using System.Collections.Generic;
using UnityEngine.AI;
using UnityEngine;

public class SpeedModifierZone : MonoBehaviour
{
    public float speedMultiplier = 2f;
    private Dictionary<NavMeshAgent, float> originalSpeeds = new Dictionary<NavMeshAgent, float>();

    void OnTriggerEnter(Collider other)
    {
        var agent = other.GetComponent<NavMeshAgent>();
        if (agent != null)
        {
            originalSpeeds[agent] = agent.speed;
            agent.speed *= speedMultiplier;
        }
    }

    void OnTriggerExit(Collider other)
    {
        var agent = other.GetComponent<NavMeshAgent>();
        if (agent != null && originalSpeeds.ContainsKey(agent))
        {
            agent.speed = originalSpeeds[agent];
            originalSpeeds.Remove(agent);
        }
    }
}