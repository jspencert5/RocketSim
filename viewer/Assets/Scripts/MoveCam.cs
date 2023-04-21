using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveCam : MonoBehaviour
{

    public GameObject objec;
    private Vector3 offset = new Vector3(1f, 4.11f, 10.73f);

    // Update is called once per frame
    void Update()
    {
        Transform targetTransform = objec.GetComponent<Transform>();

        // Calculate the desired position of the camera
        if (Movement.yPos[Movement.curI] > 0) { 
            Vector3 desiredPosition = targetTransform.position + offset;
            // Set the position of the camera to the desired position
            transform.position = desiredPosition;
        }
        
    }
}
