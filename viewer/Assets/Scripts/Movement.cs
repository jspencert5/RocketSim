<<<<<<< Updated upstream
using System;
=======
>>>>>>> Stashed changes
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Diagnostics;
<<<<<<< Updated upstream
using System.Linq;
=======
>>>>>>> Stashed changes
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using UnityEngine;

public class Movement : MonoBehaviour
{
<<<<<<< Updated upstream
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
=======
    public static float[] xPos = new float[ReadCSV.values.Count];
    public static float[] yPos = new float[ReadCSV.values.Count];
    public static float[] times = new float[ReadCSV.values.Count];

    Stopwatch stopwatch2 = new Stopwatch();

    //public Renderer objeRenderer;
    public GameObject objec;

    private bool isMoving = false;
    private bool firstLoop = true;

    int curI = 0;

    void Start()
    {
        string temp;
        string[] temps = new string[7];

        //objeRenderer = objec.GetComponent<Transform>();

        for (int i = 1; i < xPos.Length ; i++)
        {
            temp = ReadCSV.values[i].ToString();
            temps = temp.Split(',');

            times[i] = float.Parse(temps[0]);
            xPos[i] = float.Parse(temps[1]);
            yPos[i] = float.Parse(temps[2]);

            //print(xPos[i] + " " + yPos[i] + " " + times[i] + "\n");
        }
    }

    void Update()
    {
        if (isMoving)
        {
            if (firstLoop)
            {
                firstLoop = false;
                stopwatch2.Start();
            }

            if (stopwatch2.ElapsedMilliseconds * .001f < times[times.Length-1])
            {
                objec.transform.position = new Vector3(xPos[curI], yPos[curI], -15);
                
                curI = calcI(stopwatch2.ElapsedMilliseconds * .001f);

                //objec.transform.position = new Vector3(14, 0, -15);
            } else
            {
                isMoving = false;
                firstLoop = true;
                stopwatch2.Reset();
            }
>>>>>>> Stashed changes
        }
    }

    public void move ()
<<<<<<< Updated upstream
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
=======
    {
        isMoving = true;
    }

    public int calcI(float time)
    {
        for (int i = 0; i < xPos.Length; i++ )
        {
            if (times[i] > time)
            {
                return i;
            }
        }

        return xPos.Length;
>>>>>>> Stashed changes
    }
}
