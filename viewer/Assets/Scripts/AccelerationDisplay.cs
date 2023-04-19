using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using static System.Net.Mime.MediaTypeNames.Text;
using System;

public class AccelerationDisplay : MonoBehaviour
{

    private float xAcc;
    private float yAcc;
    public Text accText;

    void Update()
    {
        xAcc = Movement.xAcc[Movement.curI];
        yAcc = Movement.yAcc[Movement.curI];
        accText.text = Math.Round(Math.Sqrt(Math.Pow(xAcc, 2) + Math.Pow(yAcc, 2))).ToString();
    }

}