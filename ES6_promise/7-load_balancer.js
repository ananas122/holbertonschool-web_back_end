/**
 * Implements a load balancer for downloading files from either China or the US.
 * Uses Promise.race to return the result of the fastest download promise.
 *
 * @param {Promise} chinaDownload - The promise for downloading a file from China.
 * @param {Promise} USDownload - The promise for downloading a file from the US.
 * @returns {Promise} - A promise that resolves to the result of the fastest download promise.
 */
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
