using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class RunPython : MonoBehaviour
{
    public string pythonFileName;
    //public string nose;
    //public string body;
    //public string thruster;
    //public string angle;

    public string filePath;
    public static ArrayList values = new ArrayList();
    public void python()
    {

        string nose = GameObject.Find("NoseText (Legacy)").GetComponent<Text>().text;
        string body = GameObject.Find("BodyText (Legacy)").GetComponent<Text>().text;
        string thruster = GameObject.Find("ThrustersText (Legacy)").GetComponent<Text>().text;
        Slider angleSlider = GameObject.Find("Slider").GetComponent<Slider>();

        float angle = 90 - angleSlider.value / angleSlider.maxValue * 90;

        string pythonArgs = pythonFileName + " " + angle + " \"" + thruster + "\" \"" + body + "\" \"" + nose + "\"";

        print(pythonArgs);

        var p = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "python",
                Arguments = pythonArgs,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow = true
            }
        };

        p.Start();
        while (!p.StandardOutput.EndOfStream)
        {
            string line = p.StandardOutput.ReadLine();
            // do something with line
            print(line);
        }
        p.WaitForExit();
        values.Clear();
        ReadFile();
    }

    public void ReadFile()
    {
        try
        {
            using (StreamReader sr = new StreamReader(filePath))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    values.Add(line);
                    //print(line);
                }
            }
        }
        catch
        {
            print("Error in CSV file reading.");
        }

    }
}
