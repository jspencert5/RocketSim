using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using UnityEngine;

public class Movement : MonoBehaviour
{
    private float[] times = new float[ReadCSV.values.Count];
    public static float[] xSpeeds = new float[ReadCSV.values.Count];
    public static float[] ySpeeds = new float[ReadCSV.values.Count];
    public static float[] yPos = new float[ReadCSV.values.Count];

    private float timeStart;
    private float curTime;
    private float timePassed;

    private Stopwatch stopwatch;

    public static int i;
    // Start is called before the first frame update
    void Start()
    {
        move();
        stopwatch = new Stopwatch();
        stopwatch.Start();
    }

    // Update is called once per frame
    void Update()
    {
        if (i > times.Length - 1)
        {
            isMoving.isMovin = false;
            i--;
        }

        if (isMoving.isMovin) {
            curTime = DateTime.Now.Millisecond;
            timePassed = 0.001f * (curTime - timeStart);

            float step = ySpeeds[i] * Time.deltaTime;
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(15, yPos[i], -15), step);

            //transform.Translate(Vector3.up * ySpeeds[i] * Time.deltaTime, Camera.main.transform);
            //transform.Translate(Vector3.right * xSpeeds[i] * Time.deltaTime);
            print(stopwatch.ElapsedMilliseconds + " " + times[i] +  "\n");

            if (0.001f * stopwatch.ElapsedMilliseconds > times[i])
            {
                i++;
            }
        } else
        {
            timeStart = DateTime.Now.Millisecond;
            i = 0;
            //stopwatch.Reset();
        }
    }

    public void move ()
    {   
        string temp;
        string[] tempVals = new string[7];

        for (int i = 1; i < ReadCSV.values.Count; i++)
        {
            temp = (string)ReadCSV.values[i];
            tempVals = temp.Split(',');

            //for (int j = 0; j < 6; j++)
            //{
            //    print(tempVals[j] + "\n");
            //

            times[i] = float.Parse(tempVals[0]);
            xSpeeds[i] = float.Parse(tempVals[3]);
            ySpeeds[i] = float.Parse(tempVals[4]);
            yPos[i] = float.Parse(tempVals[2]);
        }
    }
}
