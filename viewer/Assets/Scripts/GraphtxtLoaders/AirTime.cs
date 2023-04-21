using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MaxTText : MonoBehaviour
{
    public Text Max;
    private double time;
    void Start()
    {
        time = Movement.times[Movement.times.Length - 1];
        time = Math.Round(time, 1);
        Max.text = time.ToString();
    }
}
