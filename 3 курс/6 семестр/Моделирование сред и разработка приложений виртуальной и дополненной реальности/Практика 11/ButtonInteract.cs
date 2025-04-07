using UnityEngine;

public class ButtonInteract : MonoBehaviour
{
    [Header("Particle System")]
    public ParticleSystem particleEffect;
    public float effectDuration = 3f;

    [Header("Audio Settings")]
    public bool useExplosionSound = true;
    public AudioClip localActivationSound;

    [Header("Visual Feedback")]
    public Material activatedMaterial;
    public GameObject interactionUI;

    private AudioSource audioSource;
    private Material originalMaterial;
    private Renderer buttonRenderer;
    private bool isActivated = false;

    void Start()
    {
        buttonRenderer = GetComponent<Renderer>();
        originalMaterial = buttonRenderer.material;

        audioSource = GetComponent<AudioSource>();
        if (audioSource == null)
            audioSource = gameObject.AddComponent<AudioSource>();

        if (interactionUI) interactionUI.SetActive(false);
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") && interactionUI)
            interactionUI.SetActive(true);
    }

    void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player") && interactionUI)
            interactionUI.SetActive(false);
    }

    void OnTriggerStay(Collider other)
    {
        if (other.CompareTag("Player") && Input.GetKeyDown(KeyCode.E) && !isActivated)
            ActivateEffect();
    }

    public void ActivateTrap()
    {
        if (!isActivated)
            ActivateEffect();
    }

    private void ActivateEffect()
    {
        isActivated = true;

        // Запуск эффекта частиц
        if (particleEffect != null)
            particleEffect.Play();

        // Воспроизведение звука
        if (useExplosionSound)
        {
            if (SFX_Manager.Instance != null)
                SFX_Manager.Instance.PlayExplosion();
            else
                Debug.LogWarning("SFX_Manager instance missing!");
        }
        else if (localActivationSound != null)
        {
            audioSource.PlayOneShot(localActivationSound);
        }

        // Визуальная обратная связь
        if (activatedMaterial != null)
            buttonRenderer.material = activatedMaterial;

        if (interactionUI) interactionUI.SetActive(false);

        Invoke("ResetButton", effectDuration);
    }

    private void ResetButton()
    {
        isActivated = false;
        if (particleEffect != null)
            particleEffect.Stop();

        buttonRenderer.material = originalMaterial;
    }
}