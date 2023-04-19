using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
//using static System.Net.Mime.MediaTypeNames;

public class VelocityDisplay : MonoBehaviour
{
        private float xVel;
        private float yVel;
        public Text VelText;

        void Update()
        {
            xVel = Movement.xVel[Movement.curI];
            yVel = Movement.yVel[Movement.curI];
            VelText.text = Math.Round(Math.Sqrt(Math.Pow(xVel,2) + Math.Pow(yVel, 2))).ToString();
        }

}
