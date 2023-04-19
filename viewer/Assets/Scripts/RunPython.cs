using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;

public class RunPython : MonoBehaviour
{
    public string pythonFileName;
    public string nose;
    public string body;
    public string thruster;
    public string angle;

    public string filePath;
    public static ArrayList values = new ArrayList();
    public void python()
    {
        string pythonArgs = pythonFileName + " " + angle + " " + nose + " " + body + " " + thruster;
        Process p = Process.Start("python", pythonArgs);
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
