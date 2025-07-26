import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from '../components/ui/table';
import { toast } from 'sonner';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5001/api';

const ManageResults = () => {
    const [results, setResults] = useState([]);
    const [title, setTitle] = useState('');
    const [file, setFile] = useState(null);
    const [editingResult, setEditingResult] = useState(null);

    useEffect(() => {
        fetchResults();
    }, []);

    const fetchResults = async () => {
        try {
            const response = await axios.get(`${API_BASE_URL}/results`);
            setResults(response.data);
        } catch (error) {
            console.error('Error fetching results:', error);
            toast.error('Failed to fetch results.');
        }
    };

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('title', title);
        formData.append('file', file);

        try {
            if (editingResult) {
                await axios.put(`${API_BASE_URL}/results/${editingResult.id}`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
                toast.success('Result updated successfully!');
            } else {
                await axios.post(`${API_BASE_URL}/results`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
                toast.success('Result uploaded successfully!');
            }
            setTitle('');
            setFile(null);
            setEditingResult(null);
            fetchResults();
        } catch (error) {
            console.error('Error uploading/updating result:', error);
            toast.error(`Error uploading/updating result: ${error.response?.data?.message || error.message}`);
        }
    };

    const handleEdit = (result) => {
        setEditingResult(result);
        setTitle(result.title);
        setFile(null); // Clear file input for edit
    };

    const handleDelete = async (id) => {
        if (window.confirm('Are you sure you want to delete this result?')) {
            try {
                await axios.delete(`${API_BASE_URL}/results/${id}`);
                toast.success('Result deleted successfully!');
                fetchResults();
            } catch (error) {
                console.error('Error deleting result:', error);
                toast.error('Failed to delete result.');
            }
        }
    };

    return (
        <div className="container mx-auto p-4">
            <Card className="mb-6">
                <CardHeader>
                    <CardTitle>{editingResult ? 'Edit Result' : 'Upload New Result'}</CardTitle>
                </CardHeader>
                <CardContent>
                    <form onSubmit={handleSubmit} className="space-y-4">
                        <div>
                            <Label htmlFor="title">Result Title</Label>
                            <Input
                                id="title"
                                type="text"
                                value={title}
                                onChange={(e) => setTitle(e.target.value)}
                                required
                            />
                        </div>
                        <div>
                            <Label htmlFor="file">Result File (PDF, Image, etc.)</Label>
                            <Input
                                id="file"
                                type="file"
                                onChange={handleFileChange}
                                required={!editingResult} // File is required only for new uploads
                            />
                        </div>
                        <Button type="submit">{editingResult ? 'Update Result' : 'Upload Result'}</Button>
                        {editingResult && (
                            <Button variant="outline" onClick={() => { setEditingResult(null); setTitle(''); setFile(null); }} className="ml-2">
                                Cancel Edit
                            </Button>
                        )}
                    </form>
                </CardContent>
            </Card>

            <Card>
                <CardHeader>
                    <CardTitle>Existing Results</CardTitle>
                </CardHeader>
                <CardContent>
                    {results.length === 0 ? (
                        <p>No results uploaded yet.</p>
                    ) : (
                        <Table>
                            <TableHeader>
                                <TableRow>
                                    <TableHead>Title</TableHead>
                                    <TableHead>File</TableHead>
                                    <TableHead>Uploaded At</TableHead>
                                    <TableHead>Actions</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                {results.map((result) => (
                                    <TableRow key={result.id}>
                                        <TableCell>{result.title}</TableCell>
                                        <TableCell>
                                            <a href={result.file_url} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
                                                View File
                                            </a>
                                        </TableCell>
                                        <TableCell>{new Date(result.uploaded_at).toLocaleDateString()}</TableCell>
                                        <TableCell>
                                            <Button variant="outline" size="sm" onClick={() => handleEdit(result)} className="mr-2">
                                                Edit
                                            </Button>
                                            <Button variant="destructive" size="sm" onClick={() => handleDelete(result.id)}>
                                                Delete
                                            </Button>
                                        </TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    )}
                </CardContent>
            </Card>
        </div>
    );
};

export default ManageResults;
