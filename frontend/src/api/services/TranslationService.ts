/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_translate_document_document_translation_post } from '../models/Body_translate_document_document_translation_post';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class TranslationService {
    /**
     * Get Lng Dictionary
     * @param lng
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getLngDictionaryGetDictionaryLngGet(
        lng: string,
    ): CancelablePromise<Record<string, any>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/get-dictionary/{lng}',
            path: {
                'lng': lng,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Add Word Translation
     * @param srcLng
     * @param word
     * @param translation
     * @returns any Successful Response
     * @throws ApiError
     */
    public static addWordTranslationAddToDictionaryPost(
        srcLng: string,
        word: string,
        translation: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/add-to-dictionary',
            query: {
                'src_lng': srcLng,
                'word': word,
                'translation': translation,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Translate Document
     * @param formData
     * @returns any Successful Response
     * @throws ApiError
     */
    public static translateDocumentDocumentTranslationPost(
        formData: Body_translate_document_document_translation_post,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/document-translation',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
