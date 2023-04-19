using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;
using System.Text;

public class ReadCSV : MonoBehaviour
{
    public string filePath;
    public static ArrayList values = new ArrayList();
    public void ReadFile()
    {
        try
        {
            using (StreamReader sr = new StreamReader(filePath))
            {
                string line;
                while((line = sr.ReadLine()) != null)
                {
                    values.Add(line);
                }
            }
        } 
        catch
        {
            print("Error in CSV file reading.");
        }

        //delete
<<<<<<< Updated upstream
        //foreach (var i in values)
        //{
        //    print(i + "\n");
        //}
=======
        foreach (var i in values)
        {
            //print(i + "\n");
        }
>>>>>>> Stashed changes

    }
}
