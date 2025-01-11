import React, { useState } from "react";
import { Upload, Image as ImageIcon, Loader2 } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "./components/ui/card.tsx";

const App = () => {
  const [image, setImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [caption, setCaption] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setImagePreview(URL.createObjectURL(file));
      setCaption("");
      setError("");
    }
  };

  const handleUpload = async () => {
    if (!image) {
      setError("Please select an image to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);
    setLoading(true);
    setError("");
    setCaption("");

    try {
      const response = await fetch("http://127.0.0.1:5000/generate-caption", {
        method: 'POST',
        body: formData
      });
      const data = await response.json();
      setCaption(data.caption);
    } catch (error) {
      setError("Error generating caption. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto">
        <Card className="bg-white shadow-xl">
          <CardHeader>
            <CardTitle className="text-2xl font-bold text-center text-gray-900">
              Image Caption Generator
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-6">
              {/* Image Upload Area */}
              <div className="flex flex-col items-center">
                <label
                  htmlFor="image-upload"
                  className="w-full h-64 flex flex-col items-center justify-center px-4 py-6 border-2 border-dashed rounded-lg border-gray-300 bg-gray-50 cursor-pointer hover:bg-gray-100 transition-colors"
                >
                  {imagePreview ? (
                    <img
                      src={imagePreview}
                      alt="Preview"
                      className="max-h-56 object-contain"
                    />
                  ) : (
                    <>
                      <ImageIcon className="h-12 w-12 text-gray-400" />
                      <p className="mt-2 text-sm text-gray-600">
                        Click or drag to upload an image
                      </p>
                    </>
                  )}
                  <input
                    id="image-upload"
                    type="file"
                    className="hidden"
                    onChange={handleImageChange}
                    accept="image/*"
                  />
                </label>
              </div>

              {/* Generate Button */}
              <button
                onClick={handleUpload}
                disabled={loading || !image}
                className="w-full flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                {loading ? (
                  <>
                    <Loader2 className="animate-spin -ml-1 mr-2 h-4 w-4" />
                    Generating...
                  </>
                ) : (
                  <>
                    <Upload className="-ml-1 mr-2 h-4 w-4" />
                    Generate Caption
                  </>
                )}
              </button>

              {/* Caption Display */}
              {caption && (
                <div className="mt-4 p-4 bg-green-50 rounded-md">
                  <p className="text-sm text-green-800">
                    <strong>Generated Caption:</strong> {caption}
                  </p>
                </div>
              )}

              {/* Error Display */}
              {error && (
                <div className="mt-4 p-4 bg-red-50 rounded-md">
                  <p className="text-sm text-red-800">
                    <strong>Error:</strong> {error}
                  </p>
                </div>
              )}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default App;