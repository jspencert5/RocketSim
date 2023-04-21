using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class TimeDisplay : MonoBehaviour
{

    private float time;
    public Text TimeLabel;

    // Update is called once per frame
    void Update()
    {

        time = Movement.times[Movement.curI];
        TimeSpan t = TimeSpan.FromSeconds(time);
        TimeLabel.text = "T+" + t.ToString("hh':'mm':'ss\\.ff");

    }
}
