using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class NewBehaviourScript : MonoBehaviour
{
    public int Scene1;

    public void ChangeScene()
    {
        SceneManager.LoadScene(Scene1);
    }
}
