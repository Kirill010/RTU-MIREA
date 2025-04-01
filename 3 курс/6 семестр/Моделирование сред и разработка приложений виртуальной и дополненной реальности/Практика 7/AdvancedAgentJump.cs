using UnityEngine;
using UnityEngine.AI;
using System.Collections;

public class AdvancedAgentJump : MonoBehaviour
{
    [Header("Jump Settings")]
    public float jumpHeight = 2f;
    public float jumpDuration = 1f;
    public AnimationCurve jumpCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
    public LayerMask groundLayer; // Слой для проверки земли

    private NavMeshAgent agent;
    private bool isJumping;
    private bool isGround = true;

    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        agent.autoTraverseOffMeshLink = false;
    }

    void Update()
    {
        CheckGrounded();

        // Прыжок по нажатию пробела
        if (!isJumping && isGround && Input.GetKeyDown(KeyCode.Space))
        {
            TryManualJump();
        }

        // Автоматический прыжок через Off-Mesh Link
        if (!isJumping && agent.isOnOffMeshLink)
        {
            StartCoroutine(PerformOffMeshLinkJump());
        }
    }

    void CheckGrounded()
    {
        isGround = Physics.Raycast(transform.position, Vector3.down, 0.2f, groundLayer);
    }

    void TryManualJump()
    {
        Vector3 jumpTarget = transform.position + transform.forward * agent.speed * jumpDuration;

        NavMeshHit hit;
        if (NavMesh.SamplePosition(jumpTarget, out hit, 1f, NavMesh.AllAreas))
        {
            StartCoroutine(PerformJump(transform.position, hit.position));
        }
    }

    IEnumerator PerformOffMeshLinkJump()
    {
        isJumping = true;
        OffMeshLinkData linkData = agent.currentOffMeshLinkData;
        yield return StartCoroutine(PerformJump(linkData.startPos, linkData.endPos));
        agent.CompleteOffMeshLink();
        isJumping = false;
    }

    IEnumerator PerformJump(Vector3 startPos, Vector3 endPos)
    {
        isJumping = true;
        agent.enabled = false;

        float timeElapsed = 0f;

        while (timeElapsed < jumpDuration)
        {
            float t = timeElapsed / jumpDuration;
            float height = jumpCurve.Evaluate(t) * jumpHeight;

            transform.position = Vector3.Lerp(startPos, endPos, t) + Vector3.up * height;
            timeElapsed += Time.deltaTime;
            yield return null;
        }

        transform.position = endPos;
        agent.enabled = true;
        isJumping = false;
    }
}