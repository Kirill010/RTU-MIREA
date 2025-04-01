using UnityEngine;
using UnityEngine.SceneManagement;

public class UIMainMenu : MonoBehaviour
{
    public void StartGame(string SceneName)
    {
        SceneManager.LoadScene(SceneName);
    }
    public void ExitGame()
    {
        Application.Quit();
        Debug.Log("Exit game");
    }
}
