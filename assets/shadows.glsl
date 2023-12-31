/*
 * Ray Cast Shadow Shader
 * 
 * Based on this tutorial: https://api.arcade.academy/en/latest/tutorials/raycasting/index.html
 */

#define N 50

// x, y position of the light
uniform vec2 lightPosition;
// Size of light in pixels
uniform float lightSize;
//uniform float pixelSize;

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    // Distance in pixels to the light
    float distanceToLight = distance(lightPosition, fragCoord);

    // Normalize the fragment coordinate from (0.0, 0.0) to (1.0, 1.0)
    vec2 normalizedFragCoord = fragCoord/iResolution.xy;
    vec2 normalizedLightCoord = lightPosition.xy/iResolution.xy;

    // Start our mixing variable at 1.0
    float lightAmount = 1.0;
    for( int i = 0; i < N; ++i )
    {
        // A 0.0 - 1.0 ratio between where our current pixel is, and where the light is
        float t = i/float(N);
        // Grab a coordinate between where we are and the light
        vec2 samplePoint = mix(normalizedFragCoord, normalizedLightCoord, t);

        // Is there something there? If so, we'll assume we are in shadow
        float shadowAmount = 1.0 - texture(iChannel0, samplePoint).a;
        // Multiply the light amount.
        // (Multiply in case we want to upgrade to soft shadows)
        lightAmount *= shadowAmount;

        // Exit if already black
        if( lightAmount < 0.1 ) break;
    }

    // Find out how much light we have based on the distance to our light
    lightAmount *= 1.0 - smoothstep(0.0, lightSize, distanceToLight);

    // We'll alternate our display between black and whatever is in channel 1
    vec4 blackColor = vec4(0.0, 0.0, 0.0, 1.0);

    // Our fragment color will be somewhere between black and channel 1
    // dependent on the value of b.
    fragColor = mix(blackColor, texture(iChannel1, normalizedFragCoord), lightAmount);
}
