using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Runtime.InteropServices;
using UnityEngine;
using UnityEngine.UI;

public class Rotation : MonoBehaviour
{

    public static float angle;

    public Slider sliderVal;
    public GameObject rocket;

    // Update is called once per frame
    void Update()
    {
        angle = sliderVal.value * -90;
        rocket.transform.localRotation = Quaternion.Euler(0, 0, angle);
        

    }
}
