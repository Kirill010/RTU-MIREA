using UnityEngine;

public class SFX_Manager : MonoBehaviour
{
    public static SFX_Manager Instance;

    [Header("Background Music")]
    public AudioSource musicMain;
    public AudioSource heartbeatSound;

    [Header("Sound Effects")]
    public AudioSource jumpSound;
    public AudioSource buttonClickSound;
    public AudioSource explosionSound;
    private bool isRunning = false;

    void Awake()
    {
        if (Instance == null)
            Instance = this;
        else
            Destroy(gameObject);
    }
    void Update()
    {
        // Плавное управление звуком сердцебиения
        if (isRunning && !heartbeatSound.isPlaying)
        {
            heartbeatSound.Play();
        }
        else if (!isRunning && heartbeatSound.isPlaying)
        {
            heartbeatSound.Stop();
        }
    }

    // Методы для воспроизведения звуков
    public void PlayJumpSound() => jumpSound.Play();
    public void PlayButtonClick() => buttonClickSound.Play();
    public void PlayExplosion() => explosionSound.Play();

    // Переключение музыки (например, при начале боя)
    public void SwitchToBattleMusic()
    {
        musicMain.Stop();
    }
    public void SetRunningState(bool running)
    {
        isRunning = running;

        // Можно добавить плавное изменение громкости
        if (running)
        {
            heartbeatSound.volume = Mathf.Lerp(heartbeatSound.volume, 1f, Time.deltaTime * 5f);
        }
        else
        {
            heartbeatSound.volume = Mathf.Lerp(heartbeatSound.volume, 0f, Time.deltaTime * 5f);
        }
    }
}