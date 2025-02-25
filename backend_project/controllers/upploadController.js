const AWS = require('aws-sdk');
const multer = require('multer');
const { v4: uuidv4 } = require('uuid');

const s3 = new AWS.S3();

const upload = multer({
    storage: multer.memoryStorage(),
    limits: { fileSize: 5 * 1024 * 1024 * 1024 }, // 5GB
    fileFilter: (req, file, cb) => {
        if (file.mimetype === 'audio/mpeg' || file.mimetype === 'audio/wav') {
            cb(null, true);
        } else {
            cb(new Error('Invalid file type, only MP3 and WAV is allowed!'), false);
        }
    }
}).single('file');

exports.uploadFile = (req, res) => {
    upload(req, res, async (err) => {
        if (err) {
            if (err.code === 'LIMIT_FILE_SIZE') {
                return res.status(413).json({ error: 'File size exceeds 5GB limit' });
            }
            return res.status(400).json({ error: err.message });
        }

        const file = req.file;
        if (!file) {
            return res.status(400).json({ error: 'No file uploaded' });
        }

        const fileKey = `${uuidv4()}-${file.originalname}`;
        const params = {
            Bucket: process.env.S3_BUCKET_NAME,
            Key: fileKey,
            Body: file.buffer,
            ContentType: file.mimetype,
            ACL: 'public-read'
        };

        try {
            const data = await s3.upload(params).promise();
            res.json({ id: fileKey, url: data.Location });
        } catch (uploadError) {
            console.error('Error uploading to S3:', uploadError);
            res.status(500).json({ error: 'Error uploading file' });
        }
    });
};