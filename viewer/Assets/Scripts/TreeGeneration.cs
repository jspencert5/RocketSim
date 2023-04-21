using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TreeGeneration : MonoBehaviour
{

    public int width;
    public int height;

    [Range(0.01f, 10f)]
    public float scale;

    public GameObject treePrefab1;
    public GameObject treePrefab2;
    public GameObject treePrefab3;

    [Range(0.01f, 10f)]
    public float acceptencePoint;

    void Start()
    {

        GameObject[] treeArr = {treePrefab1, treePrefab2, treePrefab3 };

        for (int y = -height; y < height; y++) {

            for (int x  = -width; x < width; x++) {

                float yValue = y / scale;
                float xValue = x / scale;

                float perlinValue = Mathf.PerlinNoise(xValue, yValue);

                if (perlinValue >= acceptencePoint) {

                    Instantiate(treeArr[Random.Range(0,2)], new Vector3(x, 0, y), Quaternion.identity);
                
                }
            
            }

        }
        
    }

    
}
