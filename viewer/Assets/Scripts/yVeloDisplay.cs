using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using static System.Net.Mime.MediaTypeNames.Text;

public class yVelocityDisplay : MonoBehaviour
{

    private float yVel;
    public Text yVelText;

    void Update()
    {
        yVel = Movement.yVel[Movement.curI];
        yVelText.text = "Y-Velocity: " + yVel.ToString();
    }

}