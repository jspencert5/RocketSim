using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SaveObjeect : MonoBehaviour
{
    void Start()
    {
        DontDestroyOnLoad(gameObject);
    }
}
