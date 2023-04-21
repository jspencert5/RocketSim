using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MaxAText : MonoBehaviour
{
    public Text Max;
    private double MVal = 0;
    private double mag = 0;
    // Start is called before the first frame update
    void Start()
    {
        for (int i = 0; i < Movement.yPos.Length - 1; i++)
        {
            mag = Math.Sqrt((Math.Pow(Movement.xAcc[i], 2) + Math.Pow(Movement.yAcc[i], 2)));

            if (mag > MVal)
            {
                MVal = mag;
            }
        }
        MVal = Math.Round(MVal);
        Max.text = MVal.ToString();
    }
}
