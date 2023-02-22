using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeMaterial : MonoBehaviour
{
    public Renderer rend;
    public GameObject obj;

    private Material[] colors;

    private int colorNum = 0;

    void Start()
    {

        rend = obj.GetComponent<rend>();
    }

    public void changeColor
    {
        colorNum++;

        if (colorNum > 2) 
        {
            colorNum = 0;
        }
    }
}
