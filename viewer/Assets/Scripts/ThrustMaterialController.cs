using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ThrustMaterialController : MonoBehaviour
{
    public static Renderer[] rendList;
        
    public Renderer objeRenderer1;
    public GameObject objec1;
    public Renderer objeRenderer2;
    public GameObject objec2;
    public Renderer objeRenderer3;
    public GameObject objec3;
    public Renderer objeRenderer4;
    public GameObject objec4;

    [SerializeField] private Color[] colors;
    private int colVal;

    void Start()
    {
        objeRenderer1 = objec1.GetComponent<Renderer>();
        objeRenderer2 = objec2.GetComponent<Renderer>();
        objeRenderer3 = objec3.GetComponent<Renderer>();
        objeRenderer4 = objec4.GetComponent<Renderer>();
    }

    public void changeMaterial()
    {
        colVal++;
        if (colVal > colors.Length - 1)
        {
            colVal = 0;
        }

        objeRenderer1.material.color = colors[colVal];
        objeRenderer2.material.color = colors[colVal];
        objeRenderer3.material.color = colors[colVal];
        objeRenderer4.material.color = colors[colVal];
    }
}
