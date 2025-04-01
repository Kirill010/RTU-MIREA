using UnityEngine;
using UnityEngine.AI;

public class ModifierZone : MonoBehaviour
{
    public enum ZoneType { SpeedBoost, SlowDown, Stop }
    public ZoneType zoneType;
    public float modifierValue = 2f;

    private void OnTriggerEnter(Collider other)
    {
        NavMeshAgent agent = other.GetComponent<NavMeshAgent>();
        if (agent != null)
        {
            switch (zoneType)
            {
                case ZoneType.SpeedBoost:
                    agent.speed *= modifierValue;
                    break;
                case ZoneType.SlowDown:
                    agent.speed /= modifierValue;
                    break;
                case ZoneType.Stop:
                    agent.isStopped = true;
                    break;
            }
        }
    }

    private void OnTriggerExit(Collider other)
    {
        NavMeshAgent agent = other.GetComponent<NavMeshAgent>();
        if (agent != null)
        {
            switch (zoneType)
            {
                case ZoneType.SpeedBoost:
                    agent.speed /= modifierValue;
                    break;
                case ZoneType.SlowDown:
                    agent.speed *= modifierValue;
                    break;
                case ZoneType.Stop:
                    agent.isStopped = false;
                    break;
            }
        }
    }
}