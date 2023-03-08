using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;

public class MaterialController : MonoBehaviour
{
    public Renderer objeRenderer;
    public GameObject objec;
    [SerializeField] private Color[] colors;
    private int colVal; 

    void Start()
    {
        objeRenderer = objec.GetComponent<Renderer>();
    }

    public void changeMaterial()
    {
        colVal++;
        if (colVal > colors.Length - 1)
        {
            colVal = 0;
        }

            objeRenderer.material.color = colors[colVal];
    }
}
