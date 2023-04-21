using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MaxYTexr : MonoBehaviour
{
    public Text yMax;
    private double yMVal = 0;
    // Start is called before the first frame update
    void Start()
    {
        for (int i = 0; i < Movement.yPos.Length - 1; i++)
        {
            if (Movement.yPos[i] > yMVal)
            {
                yMVal = Movement.yPos[i];
            }
        }
        yMVal = Math.Round(yMVal);
        yMax.text = yMVal.ToString();
    }
}
