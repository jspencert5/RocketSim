using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using TMPro;

public class GraphDataInput : MonoBehaviour
{

    List<GameObject> lines = new List<GameObject>();
    private DD_DataDiagram dd;
    private TextMeshProUGUI d0;
    private TextMeshProUGUI d1;
    private TextMeshProUGUI d2;
    private TextMeshProUGUI d3;
    public static float[] time = new float[ReadCSV.values.Count];
    public static float[] yPos = new float[ReadCSV.values.Count];
    public static float[] vel = new float[ReadCSV.values.Count];
    public static float[] accel = new float[ReadCSV.values.Count];


    void Start()
    {
        GameObject dataDiagram = GameObject.Find("DataDiagram");
        if (dataDiagram == null)
        {
            Debug.LogWarning("Data Diagram not found.");
            return;
        }
        dd = dataDiagram.GetComponent<DD_DataDiagram>();

        lines.Add(dd.AddLine("Height", Color.red));
        lines.Add(dd.AddLine("Velocity", Color.green));
        lines.Add(dd.AddLine("Acceleration", Color.blue));

        //generates events for removing lines?
        dd.PreDestroyLineEvent += (s, e) => { lines.Remove(e.line); };

        //read info from ReadCSV
        string temp;
        string[] temps = new string[7];
        float yMax = 0;
        float vMax = 0;
        float aMax = 0;

        for (int i = 1; i < time.Length; i++)
        {
            temp = ReadCSV.values[i].ToString();
            temps = temp.Split(',');

            time[i] = float.Parse(temps[0]);
            yPos[i] = float.Parse(temps[2]);
            float velX = float.Parse(temps[3]);
            float velY = float.Parse(temps[4]);
            vel[i] = (float)(Math.Sqrt(velX * velX + velY * velY));
            float accX = float.Parse(temps[5]);
            float accY = float.Parse(temps[6]);
            accel[i] = (float)(Math.Sqrt(accX * accX + accY * accY));

            //find max values
            if (yPos[i] > yMax) {
                yMax = yPos[i];
            }
            if (vel[i] > vMax) {
                vMax = vel[i];
            }
            if (accel[i] > aMax) {
                aMax = accel[i];
            }
        }

        //find datafields for maxes
        GameObject data0O = GameObject.Find("DataField"); //vel
        GameObject data1O = GameObject.Find("DataField1"); //height
        GameObject data2O = GameObject.Find("DataField2"); //accel
        GameObject data3O = GameObject.Find("DataField3"); //airtime
        GameObject data0 = data0O.transform.Find("Data").gameObject;
        GameObject data1 = data1O.transform.Find("Data").gameObject;
        GameObject data2 = data2O.transform.Find("Data").gameObject;
        GameObject data3 = data3O.transform.Find("Data").gameObject;

        if (data0 == null || data1 == null || data2 == null || data3 == null) {
            Debug.LogWarning("Data Fields not found.");
            return;
        }
        d0 = data0.GetComponent<TextMeshProUGUI>();
        d1 = data1.GetComponent<TextMeshProUGUI>();
        d2 = data2.GetComponent<TextMeshProUGUI>();
        d3 = data3.GetComponent<TextMeshProUGUI>();

        InputData();
        UpdateMaxes(yMax, vMax, aMax);
    }

    void InputData()
    {
        for (int i = 0; i < time.Length; i++) {
            dd.InputPoint(lines[0], new Vector2(time[i], yPos[i]));
            dd.InputPoint(lines[1], new Vector2(time[i], vel[i]));
            dd.InputPoint(lines[2], new Vector2(time[i], accel[i]));
        }
    }

    void UpdateMaxes(float y, float v, float a) {
        d0.SetText(v.ToString() + " m/s");
        d1.SetText(y.ToString() + " m");
        d2.SetText(a.ToString() + " m/s\xB2");
        d3.SetText(time[^1].ToString() + " s");
    }
}