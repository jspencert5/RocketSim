using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Scene3BackToScene2 : MonoBehaviour
{
    public int Scene2;

    public void ChangeScene()
    {
        SceneManager.LoadScene(Scene2);
    }
}
