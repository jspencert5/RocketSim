using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class ChangeSceneWithButton : MonoBehaviour
{

    public void loadScene(string sceneName)
    {

        if (sceneName == "Quit")
        {
            QuitGame();
            return;
        }

        SceneManager.LoadScene(sceneName);
    }

    void QuitGame()
    {
        Application.Quit();
        Debug.Log("Game is exiting");
        //Just to make sure its working
    }

}
