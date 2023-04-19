using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
//using static System.Net.Mime.MediaTypeNames;

public class xVelocityDisplay : MonoBehaviour
{
        private float xVel;
        public Text xVelText;

        void Update()
        {
            xVel = Movement.xVel[Movement.curI];
            print(Movement.curI);
            xVelText.text = "X-Velocity: " + xVel.ToString();
        }

}
