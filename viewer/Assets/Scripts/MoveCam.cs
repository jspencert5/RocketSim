using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveCam : MonoBehaviour
{
    public GameObject objec;
    private Vector3 offset = new Vector3(0f, 6.11f, 14.73f);

    // Update is called once per frame
    void Update()
    {
        // Get the Transform component of the object we want to follow
        Transform targetTransform = objec.GetComponent<Transform>();

        // Calculate the desired position of the camera
        Vector3 desiredPosition = targetTransform.position + offset;

        // Set the position of the camera to the desired position
        transform.position = desiredPosition;
    }
}
