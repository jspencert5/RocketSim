using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;

public class ThrustMatController : MonoBehaviour
{
    public Renderer objeRenderer;
    public GameObject objec;
    [SerializeField] private Material[] materials;
    public static int matVal;

    void Start()
    {
        objeRenderer = objec.GetComponent<Renderer>();
    }

    public void changeMaterial()
    {
        matVal++;
        if (matVal > materials.Length - 1)
        {
            matVal = 0;
        }

        objeRenderer.material = materials[matVal];
    }
}
