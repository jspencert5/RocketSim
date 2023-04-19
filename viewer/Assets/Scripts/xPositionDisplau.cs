using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
//using static System.Net.Mime.MediaTypeNames.Text;

public class xPositionDisplay : MonoBehaviour
{

    private float xPos;
    public Text xPosText;

    void Update()
    {

        xPos = Movement.xPos[Movement.curI];
        xPosText.text = Math.Round(xPos).ToString();
    }

}